# Goals

## Compare and Contrast
The goal for this repo is to create a document or documents that looks at the following attributes of a given bit of technology:

- underlying tech including any whitepapers or research papers for its design
- problems the tech solves
- trade-offs it makes
- best use-cases
- best when used with ...

## The final artifact

The final deliverable will be a document that surveys all the current technology out there for potential use by data teams describing the pros and cons of each, how and where to best use each, and a bit about the architectures of each so that data professionals can make better decisions and to inform the author of them as well. (mostly this actually)

## But...

But to best understand the various bits of tech like Apache Spark or Apache Hudi or Apache Iceberg or BigQuery or some other GCP (for now) managed service it would probably make more sense to understand the distinction between
or the evolution of data architectures over time:

Star / Snowflake schema'd Data Warehouse -> DataLake -> DataLakeHouse -> tbd?

## Proof-of-Concept

My home firewall filters out a lot of things. It drops packets for random hosts that are trying to connect to it all the time.

If I could tail the log of the those blocked connection attempts I could use that as a way to ingest data -- and if the volume is not enough -- I could create a SSH honey pot to attract such connections to generate more data.

Update as of: Wed Jan  4 07:58:24 PM CET 2023

Decided to spin up a [SSH honey-pot](https://en.wikipedia.org/wiki/Honeypot_(computing)) instead of exposing my local firewall logs as that's probably safer.

These two honey-pot implementations seem nice:

* https://github.com/Ex0dIa-dev/ssh-honeypot-go
* https://github.com/ashmckenzie/go-sshoney

Update as of: Sa 7. Jan 13:37:36 CET 2023

Going to use [faker](https://pypi.org/project/Faker/) to generate simulated point-of-sale data from a fictional store instead of the honey-pot.
