
import graphviz

def rep_MBR(table_content):
    s = graphviz.Digraph('MBR', filename='MAINS/Reportes/MBR.pdf',
                     node_attr={'shape': 'plaintext'})

    # print(table_content)

    s.node('struct1', table_content)
    s.view()
    # print(s)