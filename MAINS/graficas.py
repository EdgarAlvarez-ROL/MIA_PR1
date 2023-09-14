
import graphviz

def rep_MBR(table_content):
    s = graphviz.Digraph('MBR', filename='MAINS/Reportes/MBR.pdf',
                     node_attr={'shape': 'plaintext'})

    # print(table_content)

    s.node('struct1', table_content)
    s.view()
    # print(s)


def rep_FDISK(total, part1, part2, part3, part4):
    s = graphviz.Digraph('DISK', filename='MAINS/Reportes/DISK.pdf',
                     node_attr={'shape': 'plaintext'})
    if part4 > total:
        part4 = 0

    espacio_libre = total-part1-part2-part3-part4
    porcentaje = espacio_libre/total
    table_content = f"""<
<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0"> 
        <tr>
            <td>MBR</td>
            <td>ESPACIO LIBRE \n {espacio_libre}M {porcentaje}%</td>
            <td>PARTICION 1 \n {part1}</td>
            <td>PARTICION 2 \n {part2}</td>
            <td>PARTICION 3 \n {part3}</td>
            <td>PARTICION 4 \n {part4}</td>
        </tr>
</TABLE>>"""

    s.node('struct2', table_content)
    s.view()