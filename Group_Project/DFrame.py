class DFrame:
   
    #Constructor of the DFrame class
    def __init__(self, data):
        #list comprehension to get length of the lists
        exc = [len(i) for i in data.values()]
        if min(exc) != max(exc):
            raise Exception('The size of the columns in data is inconsistent.')
        self.data = data
        self.columns = list(data.keys())
        val = [len(i) for i in self.data.values()]
        self.size = [val[0], len(self.columns)]
    
    
    def get_col(self,c):
        if c == str(c):
            return self.data[c]
        elif c == int(c):
            return self.data[self.columns[c]]
    
    
    def get_row(self,n):
        return [i[n] for i in self.data.values()]
    
    
    def add_col(self, name, col):
        assert(len(col) == self.size[0]), "Inconsistent column sizes"
        self.data[name] = col
        self.columns.append(name)
        self.size[1] += 1

    
    def add_row(self, row):
        for i in range(len(row)):
            self.data[self.columns[i]].append(row[i])
        self.size[0] += 1

    
    
    def del_col(self, c):
        if c == str(c):
            del self.data[c]
            self.columns.remove(c) 
        elif c == int(c):
            del self.data[self.columns[c]]
            del self.columns[c]
        self.size[1] -= 1
        
    
    def del_row(self, n):
        for row in self.data.values():
            del row[n]
        self.size[0] -= 1
        
    
    def head(self, n = 6):
        # The method should return a new DFrame consisting of only
        # The first n rows of the DFrame from which it was called.
        new_data = {}

        for elem in self.data.items():
            new_data[elem[0]] = elem[1][:n]
        
        return DFrame(new_data)
    
    
    def filter(self, c, mode, val):
        col = self.get_col(c)
        dic = {key:[] for key in self.data.keys()}
        result = DFrame(dic)
        
        for i in range(len(col)):
            keep = False
            if mode == '<':
                keep = col[i] < val
            elif mode == '<=':
                keep = col[i] <= val
            elif mode == '>':
                keep = col[i] > val
            elif mode == '>=':
                keep = col[i] >= val
            else:
                keep = col[i] == val
            
            if keep == True:
                temp = self.get_row(i)
                result.add_row(temp)
                                                      
        return result

    
    def sort_by(self, c, reverse = False):
         # Helper Functions Argsort
        def argsort(x, reverse=False):
            tuple_list = []
            idx_list   = []
            for i in range(len(x)):
                tuple_list.append( (x[i], i) )
            sorted_tuples = sorted(tuple_list, reverse=reverse)
            for elem in sorted_tuples:
                idx_list.append(elem[1])
            return idx_list
        
        col = self.get_col(c)
        idx_list = argsort(col, reverse=reverse)
        tmpdict = {}
        for key in self.data.keys():
            tmpdict[key] = []
        result = DFrame(tmpdict)

        for i in idx_list:
            result.add_row(self.get_row(i))
        
        return result
    
    
    def mean(self,cols):
        mean_data = {}
        for c in cols:
            name = self.columns[c]
            avg = sum(self.get_col(c)) / len(self.get_col(c))
            mean_data[name] = [round(avg,8)] 
        return DFrame(mean_data)
            
    
    
    def __str__(self):
        # helper function
        def row_helper(row: list, widths: list):
            assert(len(row) == len(widths)), "row_helper row and width lengths must match."
            row_str = "| "
            
            for i in range(len(row)):
                row_str += f'{row[i]:<{widths[i]}} | '
            
            return row_str + '\n'
        
        widths = []
        # basically, get the max width for printing purposes
        for elem in self.columns:
            temp = len(elem)
            col = self.get_col(elem)
            
            for val in col:
                if len(str(val)) > temp:
                    temp = len(str(val))
            
            widths.append(temp)
        
        out = row_helper(self.columns, widths)
        # add '-' equal to the width
        out += ((sum(widths) + (3 * len(self.columns)) + 1) * '-') + '\n'
        # for in in length of value lists
        for i in range(self.size[0]):
            out += row_helper(self.get_row(i), widths)
    
        return out


        
#***********************************************************
#Name: read_file_to_dframe
#Purpose: read a data file and use the contents to create a
#DFrame object
#***********************************************************
def read_file_to_dframe(path, schema, sep):
    
    #***********************************************************
    #Name: read_file_to_list (helper function)
    #Purpose: read a data file and parse it into a list of lists
    #***********************************************************
    def read_file_to_list(path, schema, sep):
        with open(path) as fin:
            contents = fin.read()
        lines = contents.split('\n')
        data = []
        data.append(lines[0].split(sep))
        del lines[0]
        for i in range(0,len(lines)):
            data.append(process_line(lines[i],schema,sep))
        return data
    
    #***********************************************************
    #Name: process_line (helper function)
    #Purpose: read a data file and process each line in the file
    #***********************************************************        
    def process_line(line, schema, sep):
        tokens = line.split(sep)
        result = []
        for ele in range(0,len(tokens)):
            t = tokens[ele]
            dt = schema[ele]
            result.append(dt(t))
        return result
      
    rows = read_file_to_list(path, schema, sep)
#     data = {key: [] for key in rows[0]}
    data = {}
    for key in rows[0]:
        data[key] = []
        
    df = DFrame(data)
    del rows[0]
    for r in rows:
        df.add_row(r)           
    return df
    




    
    
    
    
    
    
    
    
        