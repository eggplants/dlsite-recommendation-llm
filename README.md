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

<https://zenn.dev/cloud_ace/articles/19bd3554ac8432> but with [DLSite](https://www.dlsite.com/) [voice works data](https://github.com/eggplants/dojinvoice_db)

## Deployment

[![Deploy to Render]](https://render.com/deploy?repo=https://github.com/eggplants/dlsite-recommendation-llm)

[![Website]](https://dlsite-recommendation-llm.onrender.com)

![screenshot](https://github.com/eggplants/dlsite-recommendation-llm/assets/42153744/97de9a5d-93a5-4283-be5c-5f248d4620c0)

[Deploy to Render]: <https://render.com/images/deploy-to-render-button.svg>
[Website]: <https://img.shields.io/website?label=dlsite-recommendation-llm.onrender.com&url=https%3A%2F%2Fdlsite-recommendation-llm.onrender.com>

## How to run

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
