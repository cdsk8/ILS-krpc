import krpc
import At as at

#connecting the krpc to ksp and givin a name to the script
conn = krpc.connect(name='ILS')

#Getting the reference frame, in this case its our vessel
vessel = conn.space_center.active_vessel

#Get our canvas in wich we will draw
canvas = conn.ui.stock_canvas

# Get the size of the game window in pixels
screen_size = canvas.rect_transform.size

# Add a panel to contain the UI elements
panel = canvas.add_panel()

# Position the panel on the left of the screen
rect = panel.rect_transform
rect.size = (300, 200)
rect.position = (110-(screen_size[0]/2), 0)

# Add a button to start ILS
button = panel.add_button("autoRoll")
button.rect_transform.position = (-50, 85)

# Add a button to stop ILS
button2 = panel.add_button("Kill")
button2.rect_transform.position = (-50, 55)

text3 = panel.add_text("Roll: ")
text3.rect_transform.position = (0, -40)
text3.color = (1, 1, 1)
text3.size = 18

#Add streams that activates when the selected button is clicked
button_clicked = conn.add_stream(getattr, button, 'clicked')
button2_clicked = conn.add_stream(getattr, button2, 'clicked')

while True:
    if button_clicked():
        text3.content = ("Roll: %f") % at.autoroll(vessel.surface_reference_frame)
        button.clicked = False
    if button2_cliked():
        text3.content = ("Roll: ")
        button2.clicked = False
        
