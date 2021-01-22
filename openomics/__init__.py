from __future__ import print_function, division, absolute_import
from .visualization import (umap)
from .multiomics import (MultiOmics)
from .clinical import ClinicalData
from .proteomics import (Protein)
from .genomics import (SomaticMutation, DNAMethylation, CopyNumberVariation)
from .transcriptomics import (
    ExpressionData,
    MessengerRNA,
    MicroRNA,
    LncRNA,
)
from . import database, utils

import imp
import sys

import dask.dataframe as dd
import pandas as pd

# -*- coding: utf-8 -*-
"""Top-level package for openomics."""

__author__ = """Nhat (Jonny) Tran"""
__email__ = 'nhat.tran@mavs.uta.edu'
__version__ = '0.8.4'

__BACKEND__ = "pandas"
backend = pd


def set_backend(new):
    """
    Args:
        new:
    """
    global __BACKEND__
    global backend
    assert new in ["dask", "pandas"]

    __BACKEND__ = new
    if new == "dask":
        backend = dd
    else:
        backend = pd

    for module in sys.modules.values():
        imp.reload(module)
