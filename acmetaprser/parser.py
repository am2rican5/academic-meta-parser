from __future__ import annotations

import abc
import re
from typing import Optional

import dateutil.parser
import requests
from bs4 import BeautifulSoup

from acmetaprser.base import AcademicPublication


class BaseParser(abc.ABC):
    def __init__(self, url: str, data: str = None):
        self.url = url
        self.data = data

    @staticmethod
    def from_url(cls, url: str) -> BaseParser:
        resp = requests.get(url)
        if resp.status_code != 200:
            raise Exception('Error occurred, status_code - {}, url - {}'.format(resp.status_code, url))
        return cls(url, data=resp.text)

    @abc.abstractmethod
    def parse(self) -> AcademicPublication:
        raise NotImplementedError()


class HighwirePressParser(BaseParser):
    def parse(self) -> Optional[AcademicPublication]:
        bs = BeautifulSoup(self.data, 'html.parser')

        head_tag = bs.find('head')
        if head_tag is None:
            return None

        result = AcademicPublication(source_url=self.url)
        for t in head_tag.find_all('meta'):
            t_content = t.get('content', None)
            if t_content is None:
                continue
            t_content = t_content.strip()
            match t.get('name', None):
                case 'citation_title':
                    result.title = t_content
                case 'citation_author' | 'citation_authors':
                    result.author = result.author + [s.strip() for s in t_content.split(';')]
                case 'citation_year' | 'citation_date' | 'citation_online_date' | 'citation_publication_date':
                    if re.match(r'^\d{4}$', t_content) is not None:
                        result.published_year = int(t_content)
                    else:
                        result.published_date = dateutil.parser.parse(t_content)
                case 'citation_dissertation_name':
                    result.type = t_content
                case 'citation_language':
                    result.language = t_content
                case 'citation_doi':
                    result.doi = t_content
                case 'citation_pmid':
                    result.pmid = t_content
                case 'citation_mjid':
                    result.mjid = t_content
                case 'citation_arxiv_id':
                    result.arxiv_id = t_content
                case 'citation_patent_number':
                    result.patent_number = t_content
                case 'citation_publisher':
                    result.publisher = t_content
                case 'citation_journal_title':
                    result.journal = t_content
                case 'citation_journal_abbrev':
                    result.journal_abbrev = t_content
                case 'citation_conference_title':
                    result.conference = t_content
                case 'citation_inbook_title':
                    result.book_title = t_content
                case 'citation_issn':
                    result.issn = t_content
                case 'citation_isbn':
                    result.isbn = t_content
                case 'citation_arxiv_id':
                    result.arxiv_id = t_content
                case 'citation_volume':
                    result.volume = t_content
                case 'citation_issue':
                    result.issue = t_content
                case 'citation_section':
                    result.section = t_content
                case 'citation_firstpage':
                    result.first_page = t_content
                case 'citation_lastpage':
                    result.last_page = t_content
                case 'citation_keywords':
                    result.keywords = result.keywords + [t.strip() for t in t_content.split(';')]
                case 'citation_abstract':
                    result.abstract = t_content
                case 'citation_public_url' | 'citation_pdf_url' | 'citation_fulltext_html_url' | 'citation_abstract_html_url' | 'citation_pdf_url':
                    result.urls.append(t_content)
                case _:
                    pass

        return result
