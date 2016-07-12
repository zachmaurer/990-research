import requests
import lxml import etree
import .grant
import .


#returndata = xml.xpath('//v:GrantOrContributionPdDurYrGrp', namespaces={'v':'http://www.irs.gov/efile'})

class Form:
  " " " A general purpose wrapper around lxml that provides easier parsing access to key xml attributes. " " " 
  def __init__(self, url):
    self.url = url
    self.tree = self._parseXML(url)
    self.grants = self._parseGrants()
    
  def _parseXML(self, url):
    try: 
        resp = requests.get(url)
        self.tree = etree.fromstring(resp.content)
      except (requests.exceptions.ConnectionError, requests.exceptions.HTTPError) as e:
        raise AttributeError("Requesting from url failed:   " + url ) from e
      except lxml.etree.XMLSyntaxError as e:
        raise AttributeError("Parsing XML tree failed.") from e
    
  def _parseGrants(self, url):

