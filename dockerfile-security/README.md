## Dockerfile security checker

TODO: Convert this to a GHUB app vs a PAT. More secure and higher API limit.

This is a simple little script that will scrape a repo for it's Dockerfile at a specific location. The Dockerfile can then be inspected for compliancy things like elevated run users. 

This can be built into an image with the idea that it could be run on a schedule in a Kubernetes cluster as a cron. 

Currently, if somethings found it's logged but it would be easy enough to add an alert capability, save to a collection for dashboard reporting, or push to Prometheus as a 1 or 0 value. 

## Configs
The script needs the following environment variables set although some have defaults if they are not set.

| VARIABLE         | DESCRIPTION                                                                      | DEFAULT                          | 
|------------------|----------------------------------------------------------------------------------|----------------------------------|
| GH_REPOS         | Comma separated list of repos to gather data. NOTE -- tight list...no whitespace | 'repo-compliance-scraper'                |
| GH_REPO_OWNER    | The GitHub org that owns the repo.                                               | jufkes               |
| GH_TOKEN         | GitHub token that has permissions to pull the Github api.                        | null                             |
| GH_PAGES         | Number of pages worth of data to pull from Github.                               | 1                                |
| GH_NUMBER_OF_PRS | Number of PR records to return on a single page (max: 100).                      | 100                              |