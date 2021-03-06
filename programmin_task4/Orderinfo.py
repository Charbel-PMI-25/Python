import validation



series = ['_id', 'order_status', 'amount', 'discount', 'order_date', 'shipped_date', 'customer_email']
series_types = [int, str, int, str, str, str, str]

class orderinfo:
    def __init__(self, *args):
        for i, variable_name in enumerate(series):
            setattr(self, variable_name, series_types[i](args[i]))

    def __str__(self):
        result = ""
        for variable_name in series:
            result += variable_name + " = " + str(getattr(self, variable_name)) + " "
        return result

    def __getitem__(self, item):
        if item in series:
            return getattr(self, item)
        else:
            raise IndexError

    def get_str_line_in_standard_form(self):
        result = ""
        for variable_name in series:
            result += str(getattr(self, variable_name)) + ";"
        return result[:-1]


    def put_element(self, item, data):
        validation.field_check(item, data)
        if item in series:
            return setattr(self, item, data)
        else:
            raise IndexError



    def has_element(self, element):
        for variable_name in series:
            if element.lower() in str(getattr(self, variable_name)).lower():
                return True
        return False


