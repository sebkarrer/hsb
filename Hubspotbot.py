
import hubspot

def get_last_note_from_deal(deal_id):
  """Gets the last note from a deal in HubSpot.

  Args:
    deal_id: The ID of the deal to get the note from.

  Returns:
    The text of the last note from the deal, or None if there are no notes.
  """

  client = hubspot.Client()
  notes = client.crm.deals.notes.get_all(deal_id=deal_id)
  if notes:
    last_note = notes[-1]
    return last_note.text
  else:
    return None

if __name__ == "__main__":
  deal_id = 123456
  last_note = get_last_note_from_deal(deal_id)
  if last_note:
    print("The last note from deal ID {} is: {}".format(deal_id, last_note))
  else:
    print("There are no notes for deal ID {}".format(deal_id))