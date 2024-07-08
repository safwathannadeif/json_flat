# initializing rem_val

from pathlib import Path

from json_flat.base.code.capture_state import Work_state
from json_flat.base.code.cfg_scan_capture import config
from json_flat.base.code.extrator import Interpreters
from json_flat.base.code.readjsonfile import readjson


###########################################################

#
# if config.has_option("generator", "generated_name_first_letter_identifier"):
#     letter = config.get("generator", "generated_name_first_letter_identifier")
#     w_s.set_added_name_id(letter)
#     print( w_s.added_name_id)

## config
# start


##############
class P_scan_capture():
    def pre_walk(self, v):
        # print("inp V str::::", v)
        # print(" type=", type(v))
        if type(v) == dict:
            str_v = str(v)
            # print(" Dict TYPE:: str_v=", str_v)
            if w_s.chk_and_upd(v):
                # print("inp str::::", str_v)
                # print("debug strv[0] and length:", str_v[0], " ", len(v))
                if str_v[0] == "{" and len(v) > 1:
                    return {w_s.added_name_id + w_s.__seq_no__("g_d"): v}
        return v

    #############################################################
    def walk(self, dicinp):

        # print("end Watch outer External DICT**********************************************")
        dicinp = self.pre_walk(dicinp)
        for k in dicinp:

            v = dicinp[k]
            type_as_string = v.__class__.__name__

            match (type_as_string):
                case "list":
                    l_fqn = w_s.fqn_lis_fl(k)
                    w_s.add_entity_fqn(l_fqn)
                    for vx in v:
                        vx = w_s.lis_item_2_dict(vx)
                        self.walk(vx)
                    w_s.del_complete_one_entry()

                case "dict":
                    d_fqn = w_s.fqn_dict_fl(k, v)
                    w_s.add_entity_fqn(d_fqn)
                    self.walk(v)
                    w_s.del_complete_one_entry()

                case "str" | "int" | "float" | "complex":
                    n_fqn = w_s.fqn_nvp_fl(k)

                    Interpreters.do_it(n_fqn, str(v))

                case _:
                    print("inp is unkwon")
                    raise Exception("Type:", type_as_string, " is not known")

        ##  End one DICT

    ########################################################################################
    def process(self):
        dict1 = readjson(json_path)
        if dict1.__class__.__name__ == "list":
            w_dict = Work_state.lis_2_dic_w_names(dict1)
            print("w_dict")
            print(w_dict)
            dict1 = w_dict
        self.walk(dict1)
        lis_2_app = Interpreters.make_output()
        if config.getboolean("output_lis_result", "list"):
            return lis_2_app
        print(
            "End Program...............................................................................................")


#  Main Run
########## Start scan and process ####################
## config
w_s = Work_state()
json_inp_file = config.get("inp_json_file", "absolute_path_name")
json_path = Path(json_inp_file)
# not ued sep=config.get("scan_capture","seprator")
len_gnrt = config.getint("generator", "max_random_length_name")
w_s.len_ran_genrt = len_gnrt
print("List CFG =", config.getboolean("output_lis_result", "list"))
if not config.getboolean("output_lis_result", "list"):
    p_scan_capture = P_scan_capture()
    p_scan_capture.process()
    print("File Generated:", config.get("out_file_results", "absolute_path_name"))
##############################
