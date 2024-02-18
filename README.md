# dlsite-recommendation-llm

[![PyPI](
  <https://img.shields.io/pypi/v/dlsite-recommendation-llm?color=blue>
  )](
  <https://pypi.org/project/dlsite-recommendation-llm/>
) [![ghcr](
  <https://ghcr-badge.deta.dev/eggplants/dlsite-recommendation-llm/size>
  )](
  <https://github.com/eggplants/dlsite-recommendation-llm/pkgs/container/dlsite-recommendation-llm>
) [![Maintainability](
  <https://api.codeclimate.com/v1/badges/0bdf5bc3de8b4354d064/maintainability>
  )](
  <https://codeclimate.com/github/eggplants/dlsite-recommendation-llm/maintainability>
) [![pre-commit.ci status](
  <https://results.pre-commit.ci/badge/github/eggplants/dlsite-recommendation-llm/master.svg>
  )](
  <https://results.pre-commit.ci/latest/github/eggplants/dlsite-recommendation-llm/master>
)

Reimplementation of <https://zenn.dev/cloud_ace/articles/19bd3554ac8432>, but for [DLSite](https://www.dlsite.com/) voice works!

## Deployment

[![Deploy to Render]](https://render.com/deploy?repo=https://github.com/eggplants/dlsite-recommendation-llm)

[![Website]](https://dlsite-recommendation-llm.onrender.com)

![screenshot](https://github.com/eggplants/dlsite-recommendation-llm/assets/42153744/97de9a5d-93a5-4283-be5c-5f248d4620c0)

[Deploy to Render]: <https://render.com/images/deploy-to-render-button.svg>
[Website]: <https://img.shields.io/website?label=dlsite-recommendation-llm.onrender.com&url=https%3A%2F%2Fdlsite-recommendation-llm.onrender.com>

## Configuration

You have to copy existing `.env.example` file to `.env` file and fill in to run in local.

- `PINECONE_API_KEY`: Pinecone [API key](https://docs.pinecone.io/docs/projects#api-keys)
- `PINECONE_INDEX`: Pinecone [index](https://docs.pinecone.io/docs/indexes) name
- `PINECONE_ENV`: [Pod environment](https://docs.pinecone.io/docs/indexes#pod-environments) to host index DB
- `OPENAI_API_KEY`: OpenAI [API key](https://platform.openai.com/docs/quickstart/account-setup)
- `OPENAI_API_MODEL`: OpenAI [model](https://platform.openai.com/docs/models/models)
- `OPENAI_API_TEMPERATURE`: OpenAI API [sampling temperature](https://platform.openai.com/docs/api-reference/audio/createTranscription#audio-createtranscription-temperature) (to put it simply, it is randomness)

## How to run

You can fetch data from DLSite with [eggplants/dojinvoice_db](https://github.com/eggplants/dojinvoice_db).

```bash
# Setup deps
poetry shell
poetry install

# Convert SQLite db to CSV file
python scripts/convert_db_to_csv.py <sqlite db file path>

# Create vector data from CSV data and upload to Pinecone
python scripts/add_doc_to_index.py <csv file path>

# Launch Streamlit server
drl
```
