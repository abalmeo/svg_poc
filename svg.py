import drawSvg as draw


d = draw.Drawing(100, 100, origin='center', displayInline=False)

# Draw a circle
d.append(draw.Circle(-40, -10, 30,
            fill='#ff0000'))
d.saveSvg('example.svg')