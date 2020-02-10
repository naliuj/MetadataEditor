class MetadataError(Exception):

    def __init__(self, tag):
        print(tag + ' is not compatible with this file type')
