import glob
import os

import pytest

import evacuation

data_folder = os.path.join(os.path.dirname(__file__), 'tests')
data_files = glob.glob(os.path.join(data_folder, '[0-9][0-9]'))

def get_data_files():
    for f in data_files:
        with open(f) as input, open(f'{f}.a') as expected:
            yield [''.join(input_data.strip()) for input_data in input.readlines()], ''.join(expected.readlines()).strip()

@pytest.mark.parametrize('inputs, expected', [*get_data_files()])
def test_correctness(inputs, expected):
    graph = evacuation.read_file_data(inputs)
    assert evacuation.max_flow(graph, 0, graph.size() - 1) == expected