import plotly.graph_objects as go


file = open("CupcakeInvoices.csv")

cupcakes = []
invoice_totals = []
all_invoices = 0

#variables I created to store data to be used for data visualization

choc = 0
van = 0
straw = 0

#Parsing through the csv file and saving the data I need

for line in file:
    print(line)

    currentLine = line.split(",")
    cupcakes.append(currentLine[2])

    total = float(currentLine[3])*float(currentLine[4])
    invoice_totals.append(total)
    
    all_invoices += total

file.close()

#Printouts of the multiple arrays I created from the csv file.

print()
    
for i in range(len(cupcakes)):
    if cupcakes[i] == "Chocolate":
        choc += invoice_totals[i]
    elif cupcakes[i] == "Vanilla":
        van += invoice_totals[i]
    elif cupcakes[i] == "Strawberry":
        straw += invoice_totals[i]

    print(cupcakes[i])

print()

#Formatting for the data display. Unsure where the extra digits are coming from in certain prints so I formatted to 2 decimal points

for invoice in invoice_totals:
    print("%.2f" % invoice)

print()

print("%.2f" % all_invoices)

#below is in largely code that I found in the plotly documentation for displaying data in a browser.

large_rockwell_template = dict(
    layout=go.Layout(title_font=dict(family="Rockwell", size=24))
)
fig = go.Figure(data=go.Bar(y=[choc,van,straw],x=["Chocolate", "Vanilla", "Strawberry"]))
fig.update_layout(yaxis_tickformat = '$')
fig.update_layout(title="Best-Selling Cupcakes", template=large_rockwell_template)
fig.show()