from unittest import TestCase

from acmetaprser.parser import HighwirePressParser


class TestHighwirePressParser(TestCase):
    default_highwire_test_case = """
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">

<head>
  <title>acmetaparser Test Title</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="shortcut icon" href="https://static.arxiv.org/static/browse/0.3.2.8/images/icons/favicon.ico" type="image/x-icon" />
  <link rel="stylesheet" type="text/css" media="screen" href="https://static.arxiv.org/static/browse/0.3.2.8/css/arXiv.css?v=20200727" />
  <link rel="stylesheet" type="text/css" media="print" href="https://static.arxiv.org/static/browse/0.3.2.8/css/arXiv-print.css?v=20200611" />
  <link rel="stylesheet" type="text/css" media="screen" href="https://static.arxiv.org/static/browse/0.3.2.8/css/browse_search.css" />
  <script language="javascript" src="https://static.arxiv.org/static/browse/0.3.2.8/js/accordion.js" /></script>

  <link rel="stylesheet" media="screen" type="text/css" href="https://static.arxiv.org/js/bibex-dev/bibex.css?20200709"/>
  <script src="https://static.arxiv.org/static/browse/0.3.2.8/js/mathjaxToggle.min.js" type="text/javascript"></script>
  <script src="//code.jquery.com/jquery-latest.min.js" type="text/javascript"></script>
  <script src="//cdn.jsdelivr.net/npm/js-cookie@2/src/js.cookie.min.js" type="text/javascript"></script>
  <script src="https://static.arxiv.org/static/browse/0.3.2.8/js/toggle-labs.js?20210728" type="text/javascript"></script>
  <script src="https://static.arxiv.org/static/browse/0.3.2.8/js/cite.js" type="text/javascript"></script><script type="text/javascript" src="https://arxiv-org.atlassian.net/s/d41d8cd98f00b204e9800998ecf8427e-T/zca7yc/b/13/a44af77267a987a660377e5c46e0fb64/_/download/batch/com.atlassian.jira.collector.plugin.jira-issue-collector-plugin:issuecollector/com.atlassian.jira.collector.plugin.jira-issue-collector-plugin:issuecollector.js?locale=en-US&collectorId=7a8da419"></script>
<script type="text/javascript">window.ATL_JQ_PAGE_PROPS =  {
  "triggerFunction": function(showCollectorDialog) {
    //Requires that jQuery is available!
    jQuery("#feedback-button").click(function(e) {
      e.preventDefault();
      showCollectorDialog();
    });
  },
  fieldValues: {
    "components": ["15700"],  // Jira ID for browse component
    "versions": ["14251"],    // Jira ID for browse-0.3.2 release
    "customfield_11401": window.location.href
  }
  };
</script>
  <meta name="citation_title" content="acmetaparser test title"/>
  <meta name="citation_author" content="Sejong, Daewang"/>
  <meta name="citation_author" content="Jiphyeon, Jeon"/>
  <meta name="citation_author" content="Hyeon, Lee"/>
  <meta name="citation_date" content="2021/04/14"/>
  <meta name="citation_online_date" content="2021/09/10"/>
  <meta name="citation_pdf_url" content="https://arxiv.org/pdf/1991.1024"/>
  <meta name="citation_arxiv_id" content="1991.1024"/>
  <meta name="citation_abstract" content="The Korean alphabet, known as Hangul in South Korea and Chosŏn'gŭl in North Korea, is a writing system for the Korean language created by King Sejong the Great in 1443."/>
  <meta name="twitter:site" content="@arxiv"/>
  <meta name="twitter:card" content="summary"/>
  <meta name="twitter:image" content="https://static.arxiv.org/icons/twitter/arxiv-logo-twitter-square.png"/>
  <meta name="twitter:image:alt" content="arXiv logo"/>
  <meta property="og:site_name" content="arXiv.org"/>
  <meta property="og:title" content="acmetaparser test title"/>
  <meta property="og:url" content="https://arxiv.org/abs/1991.1024"/>
  <meta property="og:description" content="The Korean alphabet, known as Hangul in South Korea and Chosŏn'gŭl in North Korea, is a writing system for the Korean language created by King Sejong the Great in 1443."/>
</head>
</html>"""

    def test_parse(self):
        parser = HighwirePressParser('', TestHighwirePressParser.default_highwire_test_case)
        result = parser.parse()

        assert result.title == 'acmetaparser test title'
        assert result.arxiv_id == '1991.1024'
        assert len(result.author) == 3
