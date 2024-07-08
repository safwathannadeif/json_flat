# Unit Separator US 0x1F Record Separator  0x1E
# EOLN = 0x1E  # End_Of_lis_name
# SOPN = 0x1f  # Start_Of_Pseudonym
'''
Lis_E_ID = Work_state.EOLN  ## End_Of_lis_name to have unique names forr any list
St_P_N = Work_state.SOPN    ## Start_Of_Pseudonym name for nvp
'''

import random
import string


# from base.code.cfg_scan_capture import config


class Work_state:
    '''
    ST_DICT = "\0x1C"
    ST_Lis = "\0x1D"
    ST_NVP = "\0x1E"
    '''

    # LIS_ITEM_NO_NAME = "\0x1F"  # Name is not real just name for items inside llist starts with letter
    lis_2_start_with = ""

    def __init__(self):
        self.track_eni_fqn_lis = []
        self.sep = ">"
        self.no_4_seq = 0
        self.no_d_seq = 0
        self.len_ran_genrt = 8
        self.added_name_id = "\u03A9"  # omega for entity without name this is the start of the genrated fake name
        self.values_processed = set()
        # self.start_with_lis=False
        # self.lis_2_start_with=""

        # self.track_eni_fqn_lis.append("root")
        # self.no_4_seq = -1

    #    def set_added_name_id(self,x):
    #           self.added_name_id=''.join([r'\u{:04X}'.format(ord(x))])
    #           self.added_name_id=x
    def chk_and_upd(self, pv):
        pv_objid = id(pv)
        # print("chk_and_upd just  inp v:", pv, "pv_objid:", pv_objid)
        if pv_objid in self.values_processed:
            # print("chk_and_upd found ", pv_objid, " return False")
            return False
        self.values_processed.add(pv_objid)
        # self.values_processed.update({pv_objid})
        # print("chk_and_upd added and  ", pv_objid, " return True")
        return True

    def fqn_nvp_fl(self, name_inp_nvp):
        sep1 = self.sep
        if len(self.track_eni_fqn_lis) == 0: sep1 = ""
        # if name_inp_nvp.startswith("$M"): add_id_letter = ""
        # fqn_nvp_id = "".join([self.get_last_fqn(), sep1, add_id_letter, str(len(name_inp_nvp)), name_inp_nvp])

        fqn_nvp_id = "".join(
            [Work_state.lis_2_start_with, self.get_last_fqn(), sep1, "N", str(len(name_inp_nvp)), name_inp_nvp])
        return fqn_nvp_id

    def fqn_lis_fl(self, lis_name_k):
        fqn_list_id = "".join(["L", str(len(lis_name_k)), lis_name_k])
        return fqn_list_id

    def fqn_dict_fl(self, name_inp_dict, v):
        # print("fqn_dict_fl::::::::/name_inp_dict", name_inp_dict)
        # print("fqn_dict_fl::::::::/name_inp_dict_v/objid", id(v))
        self.chk_and_upd(v)
        # fqn_dict_id = "".join([self.__d_seq_no__("X"), "D", str(len(name_inp_dict)), name_inp_dict])
        fqn_dict_id = "".join(["D", str(len(name_inp_dict)), name_inp_dict])
        return fqn_dict_id

    def get_last_fqn(self):
        last_inx_inlis = len(self.track_eni_fqn_lis) - 1
        if (last_inx_inlis > -1):
            return (self.track_eni_fqn_lis[last_inx_inlis])  # fqn
        return ""

    def lis_item_2_dict(self, vvxx):

        if type(vvxx) == dict:  # Only dict inside lis but the dict without name
            return vvxx
            # return {self.sep + self.__seq_no__("X"): vvxx}  # {k1:v1,....}
            # return {self.__seq_no__("$"): vvxx}  # {k1:v1,....}
        if str(vvxx).find(":") > 0:
            return vvxx  # K1:v1
        # otherwise it is list witout names so give it a name
        out_key = "".join([self.added_name_id, self._get_random_string_(self.len_ran_genrt)])
        out_dict = {out_key: vvxx}

        return out_dict

    def del_complete_one_entry(self):
        last_inx_inlis = len(self.track_eni_fqn_lis) - 1
        del self.track_eni_fqn_lis[last_inx_inlis]

    def add_entity_fqn(self, fqn):
        sep1 = self.sep
        if self.track_eni_fqn_lis == "":
            self.track_eni_fqn_lis.append("".join([self.get_last_fqn(), fqn]))
            return
        self.track_eni_fqn_lis.append("".join([self.get_last_fqn(), sep1, fqn]))
        # self.track_eni_fqn_lis.append(self.get_last_fqn())     #Not working

    def _get_random_string_(self, length):
        rand_str = ''.join(random.choice(string.ascii_letters) for i in range(length))
        return (rand_str)

    def __seq_no__(self, letter):
        self.no_4_seq += 1
        return letter + str(self.no_4_seq)  # i += 1

    def __d_seq_no__(self, letter):
        self.no_d_seq += 1
        return str(self.no_d_seq) + letter  # i += 1

    @staticmethod
    def lis_2_dic_w_names(inls):
        Work_state.lis_2_start_with = ">L4sb_0"  # constant for json starts with list [
        genkeys = list(map(lambda x: "sq_" + str(x), range(0, len(inls))))
        my_dict1 = dict(zip(genkeys, inls))  # zip the lis, keys pairs to generate the dict
        return (my_dict1)
