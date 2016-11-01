import unittest
import os
import pandas as pd
import numpy.testing as npytest
import data_cleanup_toolbox as data_cln


class TestSanity_check_data_file(unittest.TestCase):
    def setUp(self):
        self.input_df_good = pd.DataFrame(
            [[1, 0],
             [0, 0],
             [1, 1]],
            index=['ENSG00000000003', "ENSG00000000457", 'ENSG00000000005'],
            columns=['a', 'b']
        )
        self.input_phenotype = pd.DataFrame(
            [[1.1, 2.2, 3.3]],
            index=['drug1'],
            columns=['a', 'b', 'c']
        )

        self.run_parameters = {
            "spreadsheet_name_full_path": "../data/spreadsheets/example.tsv",
            "phenotype_full_path": ".. /data/spreadsheets/phenotype.tsv",
            "results_directory": "./",
            "redis_credential": {
                "host": "knownbs.dyndns.org",
                "port": 6380,
                "password": "KnowEnG"
            },
            "source_hint": "",
            "taxonid": '9606',
            "pipeline_type": "gene_priorization_pipeline",
            "input_data_type": ""
        }

        self.output_ensemble = "./example_ETL.tsv"
        self.output_mapped = "./example_MAP.tsv"
        self.output_unmapped = "./example_UNMAPPED.tsv"
        self.output_phenotype_cleaned = "./phenotype_ETL.tsv"

    def tearDown(self):
        del self.input_df_good
        del self.run_parameters
        os.remove(self.output_mapped)
        os.remove(self.output_ensemble)
        os.remove(self.output_unmapped)
        os.remove(self.output_phenotype_cleaned)
        del self.output_mapped
        del self.output_ensemble
        del self.output_unmapped
        del self.output_phenotype_cleaned

    def test_sanity_check_data_file(self):
        ret_val, ret_msg = data_cln.sanity_check_data_file(self.input_df_good, self.input_phenotype, self.run_parameters)
        self.assertEqual(True, ret_val)


if __name__ == '__main__':
    unittest.main()
