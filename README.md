## Performing full text search with the Supabase Python library

This is a Python project demonstrating full text search with the Supabase Python library. This project is a part of this blog post https://www.donielsmith.com/blog/supabase-full-text-search-in-python/

Requirements:

- Python 3.11+
- Poetry 1.8.2+


### Installation

You can get started by running the following command in the root directory of this project once you have cloned it.

```shell
poetry install
```

You can rename the `example.env` in the root directory to `.env` and update the values to match your Supabase instance.

> Note: if you are using the Supabase CLI locally the values already in the `example.env` file should work by default.

If you want to run this project locally using the [Supabase CLI](https://supabase.com/docs/guides/cli/getting-started) you can run:

```shell
npx supabase start
```

### Testing the project

In order to test this project you can change into the poetry shell and run the project with Python executable.

```shell
poetry shell
python supabase_full_text_search/main.py
```

