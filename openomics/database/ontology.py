import pandas as pd
from Bio.UniProt import GOA

from .annotation import Dataset


class GeneOntology(Dataset):
    COLUMNS_RENAME_DICT = {
        "DB_Object_Symbol": "gene_name",
        "DB_Object_ID": "gene_id",
        "GO_ID": "go_id"
    }

    def __init__(self, path="http://geneontology.org/gene-associations/",
                 file_resources=None, col_rename=COLUMNS_RENAME_DICT, npartitions=0):
        if file_resources is None:
            file_resources = {"goa_human.gaf": "goa_human.gaf.gz",
                              "go-basic.obo": "http://purl.obolibrary.org/obo/go/go-basic.obo",
                              "goa_human_rna.gaf": "goa_human_rna.gaf.gz",
                              "goa_human_isoform.gaf.gz": "goa_human_isoform.gaf.gz"
                              }
        super(GeneOntology, self).__init__(path, file_resources, col_rename=col_rename, npartitions=npartitions)

    def load_dataframe(self, file_resources):
        lines = []
        dfs = []
        for file in self.file_resources:
            if file == "go-basic.obo": continue

            l = GOA.gafiterator(self.file_resources[file])
            for line in l:
                lines.append(line)
            go_df = pd.DataFrame(lines)
            dfs.append(go_df)

        go_df = pd.concat(dfs)
        return go_df
