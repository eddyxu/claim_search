import argparse
import logging
import json
from pathlib import Path
import polars as pl

from claim_search.schema import Claim, Email, Attachment
import lancedb


def ingest_data(args):
    """Ingest data"""
    logging.info("Ingesting data from %s", args.data)
    base_path = Path(args.data)

    db = lancedb.connect("claims.db")

    claims = pl.read_json(base_path / "claims.json")
    db.create_table("claims", schema=Claim, data=claims)

    emails = pl.read_json(base_path / "emails.json")
    db.create_table("emails", schema=Email, data=emails)

    attachments = pl.read_json(base_path / "attachments.json")
    db.create_table("attachments", schema=Attachment, data=attachments)


def main():
    parser = argparse.ArgumentParser(description="Claim Search CLI")

    subparsers = parser.add_subparsers(dest="command")
    subparsers.required = True

    ingest = subparsers.add_parser("ingest", help="Ingest data")
    ingest.add_argument(
        "data",
        type=str,
        metavar="DIR",
        help="Path to the data files to ingest",
    )
    ingest.set_defaults(func=ingest_data)

    args = parser.parse_args()
    args.func(args)
