# Gives the Hierarchy Identifiers  Full-Qualified-Name --fqn
import re

from json_flat.base.code.cfg_scan_capture import config

list_out_4wiring = config.getboolean("output_lis_result", "list")
out_filename = config.get("out_file_results", "absolute_path_name")


class Interpreters:
    extrator_lis = []
    added_name_id = '\u03A9'  # omega
    wire_out_lis = []

    @staticmethod
    def make_output():

        if not list_out_4wiring:  # no lis
            col_width = max(len(word) for row in Interpreters.extrator_lis for word in row[1:]) + 2  # padding
            header = ["#Token Names", "Composed Name", "Value", "   Interpretation"]
            with open(out_filename, 'w') as f:
                print("".join(h.ljust(col_width) for h in header), file=f)
                # print("".join(["XXXX","YYYYY","cccccc","BBBBBBBBBBB"].ljust(col_width) ), " ",  file=f)
                for row in Interpreters.extrator_lis:
                    # print("".join(word.ljust(col_width) for word in row), file=f)

                    print("".join(word.ljust(col_width) for word in row[1:]), " ", row[0], file=f)

        else:
            # out_lis_4wire = [x[1:3]for x in Interpreters.extrator_lis]
            # out_lis_4wire =
            for row in Interpreters.extrator_lis:
                Interpreters.wire_out_lis.append([row[2], row[3]])

            # for w1,w2 in out_lis_4wire:
            #         print("wiring Integration out:", w1,w2)
            #
            return Interpreters.wire_out_lis

    ##############################################################
    @staticmethod
    def do_it(fqni, vi):

        value = vi
        herarchyIds = ""
        token_4more_process = ""
        entry_w_value = ""
        # print("##inp::", fqni, "value::", value)
        by_type_lis = re.findall(r'[D,L,N]\w+', fqni)
        for ix in range(0, len(by_type_lis)):
            letter = by_type_lis[ix][0]
            length_word = -1
            i = 1
            collected_digits = ""
            while i < len(by_type_lis[ix]):
                if by_type_lis[ix][i].isdigit():
                    collected_digits = collected_digits + by_type_lis[ix][i]  # joint is better
                if not by_type_lis[ix][i].isdigit(): break
                i += i
            # print("Watch.....collected_digits[", collected_digits,"]", len(collected_digits))
            if len(collected_digits) == 0: continue  # some fun here from python
            ll = int(collected_digits)
            st = 2
            if ll >= 10: st = 3
            namex = by_type_lis[ix][st:]
            _identifer = namex
            if by_type_lis[ix].find(Interpreters.added_name_id) > 0:
                _identifer = by_type_lis[ix][st + 1:]
                namex = " "

            token_4more_process = "".join([token_4more_process, "[", _identifer, "]"])
            entry_w_value = "".join([entry_w_value, _identifer])
            match (letter):
                case "D":
                    # print(by_type_lis[ix], " is dict and inp length=", ll, " dict name {", namex, "}",
                    #       "level_identifer:", _identifer)
                    herarchyIds = "".join([herarchyIds, ">Dict:name[", namex, "]Id[", _identifer, "]"])

                case "L":
                    # print(by_type_lis[ix], " is list and length=", ll, " list name =[", namex, "]", "level_identifer:",
                    #       _identifer)
                    herarchyIds = "".join([herarchyIds, ">List:name[", namex, "]Id[", _identifer, "]"])
                case "N":
                    # print(by_type_lis[ix], " is nvp and length=", ll, " nvp name =(", namex, ")", "level_identifer:",
                    #       _identifer)
                    herarchyIds = "".join([herarchyIds, ">N4V:name[", namex, "]Id[", _identifer, "]"])
                    ############################# Debug $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
                    # print("Entry and Value list Item::",entry_w_value , " Value= " , value)
                    # print("Fqn-Interpretation::", herarchyIds, "  value=", value)
                    # print("Further Processing As Tokens and Value::", token_more_process, "value=", value)
                    ############################# Debug $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
                    Interpreters.extrator_lis.append((herarchyIds, token_4more_process, entry_w_value, value))
