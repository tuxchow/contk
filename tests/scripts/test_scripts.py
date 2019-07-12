import os
import pytest
from cotk.scripts.main import dispatch
import re
import json
import subprocess
from subprocess import PIPE
import shutil

class TestScripts():

	@pytest.mark.parametrize('url, error, match', \
		[("http://wrong_url", ValueError, "can't match any pattern"),\
		('user/repo/commit/wrong_commit', RuntimeError, "It should be public."),\
		('http://github.com/thu-coai/cotk-test-CVAE/no_result_file/', FileNotFoundError, r"Config file .* is not found."),\
		('https://github.com/thu-coai/cotk-test-CVAE/tree/invalid_json', json.JSONDecodeError, ""),\
		('thu-coai/cotk-test-CVAE/tree/keys_undefined', RuntimeError, "Undefined keys"),\
		])
	def test_download_error(self, url, error, match):
		with pytest.raises(error, match=match):
			dispatch('download', [url])

	def test_download(self):
		# with pytest.raises(FileNotFoundError) as excinfo:
		# 	report.dispatch('download', \
		# 					['--zip_url', 'https://github.com/thu-coai/cotk-test-CVAE/archive/no_output.zip'])
		# assert "New result file not found." == str(excinfo.value)
		dispatch('download', ['https://github.com/thu-coai/cotk-test-CVAE/tree/run_and_test'])

	def test_config_error(self):
		with pytest.raises(RuntimeError, match="Token cannot be empty."):
			dispatch('config', [])

	def test_config(self):
		dispatch('config', ['--token', 'token'])

	def test_import_local_resources(self):
		shutil.copyfile('./tests/_utils/dummy_coai/test.json', './cotk/resource_config/test.json')

		dispatch('import', ['--file_id', 'resources://test', '--file_path', './tests/_utils/data/test.zip'])

		os.remove('./cotk/resource_config/test.json')
