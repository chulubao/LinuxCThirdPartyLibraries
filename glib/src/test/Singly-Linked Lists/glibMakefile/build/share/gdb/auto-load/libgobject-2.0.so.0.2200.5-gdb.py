import sys
import gdb

# Update module path.
dir = '/root/glibproject/lib/share/glib-2.0/gdb'
if not dir in sys.path:
    sys.path.insert(0, dir)

from gobject import register
register (gdb.current_objfile ())
