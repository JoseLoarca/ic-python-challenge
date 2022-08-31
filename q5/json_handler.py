import json
from datetime import datetime


def claim_reader(file_name='claim.json'):
    """
    Read a JSON file, find relevant data, update timestamps and
    write to a new JSON file
    :param file_name: name of the JSON file to read
    :return: None
    """
    # Read the JSON file
    with open(file_name, 'r') as f:
        data = json.load(f)

        # Get the payee ID
        payee_id = data['payee']['id']
        print('Payee ID: {}'.format(payee_id))

        # Find any invoices that contain the text "583"
        invoices = [inv for inv in data['invoiceIds'] if '583' in inv]
        print('Invoices: {}'.format(', '.join(invoices)))

        # Convert the timestamps to format %Y-%m-%dT%H:%M:%S.
        # Divide by 1000 to avoid out of range error
        new_claim_date_time = datetime\
            .fromtimestamp(data['claimDateTime'] / 1e3)\
            .strftime('%Y-%m-%dT%H:%M:%S')

        new_file_date_time = datetime\
            .fromtimestamp(data['fileDateTime'] / 1e3)\
            .strftime('%Y-%m-%dT%H:%M:%S')

        new_received_date_time = datetime\
            .fromtimestamp(data['receivedDateTime'] / 1e3)\
            .strftime('%Y-%m-%dT%H:%M:%S')

        # Update the timestamps in the JSON file
        data['claimDateTime'] = new_claim_date_time
        data['fileDateTime'] = new_file_date_time
        data['receivedDateTime'] = new_received_date_time

        # Write the updated JSON file
        with open('new_claim.json', 'w') as nf:
            json.dump(data, nf, indent=4)
