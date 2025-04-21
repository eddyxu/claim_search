from lancedb.pydantic import LanceModel


class Claim(LanceModel):
    claim_number: str
    facts_of_loss: str
    incident_type: str
    date_of_loss: str


class Email(LanceModel):
    claim_number: str
    text_body: str
