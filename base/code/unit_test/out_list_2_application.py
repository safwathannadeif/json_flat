#
# #Application to collect the list for further processing  Test Demo
# 1 scan_capture.ini : set list=True as shown below
#
# [output_lis_result]
# list=True
# #
# import sys
# sys.path.append('base.code.')

from json_flat.base.code.extrator import Interpreters
from json_flat.base.code.scan_capture import P_scan_capture

print("Satrt Appliction Wirring to the Fallter:")
p_scan_capture = P_scan_capture()
Interpreters.wire_out_lis = p_scan_capture.process()

width = max(len(word) for row in Interpreters.wire_out_lis for word in row) + 2  # padding
head = ["fqn", "value"]
print("".join(word.ljust(width) for word in head))
for row in Interpreters.wire_out_lis:
    print("".join(word.ljust(width) for word in row))

print("End Wiring")
