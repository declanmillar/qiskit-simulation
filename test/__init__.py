# This code is part of Qiskit.
#
# (C) Copyright IBM 2024.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""Tests."""

from collections.abc import Iterable, Sequence

from qiskit_simulation import __version__


def test_version():
    """Version test."""
    assert __version__ == "0.0.0"


################################################################################
## DEFINITIONS
################################################################################
TYPES = [
    INT := 0,
    FLOAT := 0.0,
    NAN := float("NaN"),
    INF := float("Inf"),
    MINF := float("-Inf"),
    COMPLEX := complex(0, 0),
    STR := "0",
    BOOL := True,
    NONE := None,
    LIST := [0],
    TUPLE := (0,),
    DICT := {0: 0},
]
NO_INTS = [t for t in TYPES if not isinstance(t, int)]
NO_NONE = [t for t in TYPES if t is not None]
NO_INTS_NONE = [t for t in NO_INTS if t is not None]
NO_REAL = [t for t in NO_INTS if not isinstance(t, float)]
NO_NUM = [t for t in NO_REAL if not isinstance(t, complex)]
ITERS = [t for t in TYPES if isinstance(t, Iterable)]
NO_ITERS = [t for t in TYPES if not isinstance(t, Iterable)]
NO_ITERS_NONE = [t for t in NO_ITERS if t is not None]
NO_SEQS = [t for t in TYPES if not isinstance(t, Sequence)]
NO_SEQS_NONE = [t for t in NO_SEQS if t is not None]


################################################################################
## ALL
################################################################################
__all__ = [
    "TYPES",
    "NO_INTS",
    "NO_NONE",
    "NO_INTS_NONE",
    "NO_REAL",
    "NO_NUM",
    "ITERS",
    "NO_ITERS",
    "NO_ITERS_NONE",
    "NO_SEQS",
    "NO_SEQS_NONE",
]
