#!/usr/bin/env python
import sys

if len(sys.argv) != 3:
    print("Please input .world file to modify, and number of actors to add")
    print("python3 generate_actor_xml.py /home/user/gazebo.world 30")
    exit()

world_file = sys.argv[1]
num_agents = int(sys.argv[2])

f = open(world_file, "r+")
contents = f.readlines()

# Find world tag
actor_insert_line = 0
for i in range(len(contents)):
    if contents[i].find('<world') != -1:
        actor_insert_line = i + 1
        break

for i in range(num_agents):
    actor_name = "walking" + str(i)
    contents.insert(actor_insert_line, '\t\t</actor>\n')
    contents.insert(actor_insert_line, '\t\t\t</plugin>\n')
    contents.insert(actor_insert_line, '\t\t\t\t<actor_id>' + str(i) + '</actor_id>\n')
    contents.insert(actor_insert_line, '\t\t\t<plugin name="actor' + str(i) + '_plugin" filename="libactor_plugin.so">\n')
    contents.insert(actor_insert_line, '\t\t\t</animation>\n')
    contents.insert(actor_insert_line, '\t\t\t\t<interpolate_x>true</interpolate_x>\n')
    contents.insert(actor_insert_line, '\t\t\t\t<filename>walk.dae</filename>\n')
    contents.insert(actor_insert_line, '\t\t\t<animation name="walking">\n')
    contents.insert(actor_insert_line, '\t\t\t</skin>\n')
    contents.insert(actor_insert_line, '\t\t\t\t<filename>walk.dae</filename>\n')
    contents.insert(actor_insert_line, '\t\t\t<skin>\n')
    contents.insert(actor_insert_line, '\t\t\t<pose>' + str(i) + ' 0 1.0 0 0 0</pose>\n')
    contents.insert(actor_insert_line, '\t\t<actor name="' + actor_name + '">\n')
    # print('<actor name="' + actor_name + '">')
    # print('<pose>' + str(i) + ' 0 1.0 0 0 0</pose>')
    # print('<skin>')
    # print('<filename>walk.dae</filename>')
    # print('</skin>')
    # print('<animation name="walking">')
    # print('<filename>walk.dae</filename>')
    # print('<interpolate_x>true</interpolate_x>')
    # print('</animation>')
    # print('<plugin name="actor' + str(i) + '_plugin" filename="libactor_plugin.so">')
    # print('<actor_id>' + str(i) + '</actor_id>')
    # print('</plugin>')
    # print('</actor>')

f.seek(0)
f.writelines(contents)
f.truncate()
f.close()