from xml.etree.ElementTree import Element, SubElement, tostring
from xml.sax.saxutils import escape


class IliasFile:
    # see https://fossies.org/linux/ILIAS/xml/ilias_file_3_8.dtd

    def __init__(self, filename, title=None, description=None, content=None, versions=()):
        self.filename = filename
        self.title = title
        self.description = description
        self.content = content
        self.versions = versions

    def to_string(self):
        file_element = Element('File')

        filename_element = Element('Filename')
        filename_element.text = self.filename
        file_element.append(filename_element)

        if self.title:
            title_element = SubElement(file_element, 'Title')
            title_element.text = self.title

        if self.description:
            description_element = SubElement(file_element, 'Description')
            description_element.text = self.description

        if self.content:
            content_element = SubElement(file_element, 'Content')
            content_element.set('mode', 'PLAIN')
            content_element.text = escape(self.content)

        versions_element = SubElement(file_element, 'Versions')
        for version in self.versions:
            versions_element.append(version.to_element())

        return tostring(file_element)


class Version:

    def __init__(self, version_id, user_id, date):
        self.version_id = version_id
        self.user_id = user_id
        self.date = date

    def to_element(self):
        element = Element('Version')
        element.set('id', self.version_id)
        element.set('usr_id', self.user_id)
        element.set('date', self.date)
        return element
