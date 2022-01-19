import datetime
from dataclasses import dataclass, field
from datetime import date


@dataclass
class AcademicPublication:
    source_url: str = None
    title: str = None
    author: list[str] = field(default_factory=list)
    author_info: list[str] = field(default_factory=list)
    published_year: int = None
    published_date: date = None
    type: str = None
    language: str = None
    doi: str = None
    pmid: str = None
    mjid: str = None
    arxiv_id: str = None
    patent_number: str = None
    publisher: str = None
    journal: str = None
    journal_abbrev: str = None
    conference: str = None
    book_title: str = None
    issn: str = None
    isbn: str = None
    volume: str = None
    issue: str = None
    section: str = None
    first_page: str = None
    last_page: str = None
    keywords: list[str] = field(default_factory=list)
    abstract: str = None
    references: list[str] = field(default_factory=list)
    urls: list[str] = field(default_factory=list)

    def to_serializable(self):
        result = {
            i: getattr(self, i) for i in dir(self)
            if not i.startswith('__') and not callable(getattr(self, i))
        }

        for k, v in result.items():
            if isinstance(v, datetime.datetime):
                result[k] = v.isoformat()

        return result
