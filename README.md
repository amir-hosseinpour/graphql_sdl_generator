# GQL to SDL Converter

This script reads `.gql` files from a specified directory or a list of files, processes the SDL content, builds a GraphQL schema, optionally extends the schema with custom elements, and writes the final schema to an output file with an `.sdl` extension.

## Requirements

- Python 3.x
- `graphql` library

You can install the `graphql` library using pip:

```sh
pip install graphql-core
```

## Usage

```sh
python main.py [options] [arguments]
```

### Options

- `-d directory_path output_file.sdl`
  - Read `.gql` files from the specified directory and write the schema to `output_file.sdl`.
- `-f file1.gql file2.gql ... output_file.sdl`
  - Read the specified `.gql` files and write the schema to `output_file.sdl`.
- `-h`
  - Show this help message.

### Examples

#### Directory Mode

Read all `.gql` files from the specified directory and write the schema to `output_schema.sdl`:

```sh
python main.py -d /path/to/directory output_schema.sdl
```

#### File List Mode

Read the specified `.gql` files and write the schema to `output_schema.sdl`:

```sh
python main.py -f /path/to/file1.gql /path/to/file2.gql output_schema.sdl
```

## Script Details

### Functions

- **read_gql_files_from_directory(directory)**
  - Reads `.gql` files from a given directory and returns their content as a single string.

- **read_gql_files_from_list(file_list)**
  - Reads `.gql` files from a provided list of file paths and returns their content as a single string.

- **write_schema_to_file(schema_content, output_file)**
  - Writes the processed schema content to the specified output file.

- **extend_schema_with_custom_elements(schema)**
  - Placeholder function to add custom schema extensions.

- **sdl_to_python(sdl_content, output_file)**
  - Processes SDL content, builds the schema, optionally extends it, and writes the final schema to an output file.

- **print_help()**
  - Prints the help message explaining each switch and its usage.

### Main Function

The `main()` function handles the command-line arguments and calls the appropriate functions based on the provided switches (`-d`, `-f`, or `-h`).

## Notes

- Ensure the `.gql` files are correctly formatted for the script to process them without errors.
- Customize the `extend_schema_with_custom_elements(schema)` function to add any specific schema extensions as needed.
