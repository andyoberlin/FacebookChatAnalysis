from optparse import OptionParser

from analysis.WordAnalysis import WordAnalysis
from analysis.ContentAnalysis import ContentAnalysis

if __name__ == '__main__':
    parser = OptionParser()
    
    parser.add_option("-d", "--database", dest="database", default="messages.db",
                      help="Filename for the sqlite database for the messages")
    #parser.add_option("-f", "--format", dest="format", default="tabbed",
    #                  help="The format in which to output the data to the console: csv, tabbed")
    
    (opts, args) = parser.parse_args()
    
    #perform word analysis
    WordAnalysis(opts.database).analyze()
    ContentAnalysis(opts.database).analyze()
    
    
    


