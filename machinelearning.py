def op_mp(p_size) :
    def _op_mp(s_in, f):
        if f :
            return s_in / p_size
        else :
            return s_in * p_size
    return _op_mp
def op_conv(k_size) :
    def _op_conv(s_in, f) : 
        if f :
            return s_in - k_size +1
        else :
            return s_in + k_size -1
    return _op_conv
def process_op(op_list, init_val, f=False):
    if not f:
        op_list.reverse()
    data = [init_val]
    val = init_val
    for op in op_list:
        val = op(val, f)
        data.append(val)
    if not f:
        data.reverse()
    return data
def print_op(data_list):
    for index, size in enumerate(data_list):
        print("Layer", index, ":", size)