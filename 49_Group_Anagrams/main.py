class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        trans_strs = [0] * len(strs)
        a_len = len(strs)
        str_len = [0] * a_len
        grouped_strs = []
        attr_value = 1
        zero_value = 0
        j = 0
        alphatonum = {}

        gidx = 0

        for i in range (0, a_len):
            str_len[i] = len(strs[i])
            if str_len[i] == 0:
                if zero_value == 0:
                    zero_value = attr_value
                    j += 2
                    attr_value = 10 ** j
                    
                trans_strs[i] += zero_value
                
                        
            for k in range (0,str_len[i]):
                
                if strs[i][k] in alphatonum:
                    pass
                else:
                    alphatonum[strs[i][k]] = attr_value
                    j += 2
                    attr_value = 10 ** j
                trans_strs[i] += alphatonum[strs[i][k]]
                
                
        for i in range (0, len(strs)):
            if trans_strs[i] != 0:
                grouped_strs.append([])
                grouped_strs[gidx].append(strs[i])
                for k in range (i+1, len(strs)):
                    if trans_strs[i] == trans_strs[k]:
                        grouped_strs[gidx].append(strs[k])
                        trans_strs[k] = 0
                gidx += 1

        return grouped_strs
