#
# auto-pts - The Bluetooth PTS Automation Framework
#
# This program is free software; you can redistribute it and/or modify it
# under the terms and conditions of the GNU General Public License,
# version 2, as published by the Free Software Foundation.
#
# This program is distributed in the hope it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
# more details.
#

supported_projects = ['zephyr']


board_type = 'cyw920829m2evk_02'


def reset_cmd(iutctl):
    """Return reset command for cyw920829m2evk_02 DUT

    Dependency: openocd
    """

    return 'C:/Users/SingRavinder/ModusToolbox/tools_3.3/openocd/bin/openocd.exe -s C:/Users/SingRavinder/ModusToolbox/tools_3.3/openocd/scripts -f interface/kitprog3.cfg -f target/cyw20829.cfg -c "init; reset; init; shutdown; sleep 2000"'
