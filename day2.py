clients = [{"names": "MARS", "Services": "EDI Integrator"}, 
           {"names": "Reckitt", "Services": "Cloud Migration"}, 
           {"names": "SC Johnson", "Services": "API Setup"}]
for client in clients:
    print (f"Client: {client['names']} - Services: {client['Services']}")
