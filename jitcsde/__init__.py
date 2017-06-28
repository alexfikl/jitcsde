from __future__ import absolute_import
from ._jitcsde import (
		jitcsde, jitcsde_jump,
		t, y,
		UnsuccessfulIntegration,
		DEFAULT_COMPILE_ARGS,
		)

try:
	from .version import version as __version__
except ImportError:
	from warnings import warn
	warn('Failed to find (autogenerated) version.py. Do not worry about this unless you really need to know the version.')
