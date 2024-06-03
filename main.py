import sys
import os
from graphql import (
    build_ast_schema,
    parse,
    GraphQLScalarType,
    GraphQLDirective,
    DirectiveLocation,
    GraphQLArgument,
    GraphQLString,
    print_schema,
)
from graphql.language import StringValueNode

# Custom scalar type for DateTime
DateTime = GraphQLScalarType(
    name="DateTime",
    description="A custom scalar for DateTime",
    serialize=lambda x: x.isoformat() if hasattr(x, "isoformat") else x,
    parse_value=lambda x: x,
    parse_literal=lambda node, _: node.value if isinstance(node, StringValueNode) else None,
)

# Example directive definition
RestrictToSelfDirective = GraphQLDirective(
    name="restrictToSelf",
    locations=[DirectiveLocation.FIELD_DEFINITION],
    args={
        "reason": GraphQLArgument(GraphQLString, default_value="restricted"),
    }
)

# Extend schema with custom types and directives
def extend_schema_with_custom_elements(schema):
    # Add custom scalar types
    schema.type_map["DateTime"] = DateTime

    # Convert schema directives to list, add custom directive, and convert back to tuple
    schema.directives = tuple(list(schema.directives) + [RestrictToSelfDirective])

def read_gql_files_from_directory(directory):
    sdl_contents = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.gql'):
                with open(os.path.join(root, file), 'r') as f:
                    sdl_contents.append(f.read())
    return "\n".join(sdl_contents)

def read_gql_files_from_list(file_list):
    sdl_contents = []
    for file in file_list:
        if file.endswith('.gql'):
            with open(file, 'r') as f:
                sdl_contents.append(f.read())
    return "\n".join(sdl_contents)

def sdl_to_schema_file(sdl_content, output_file):
        # Parse the SDL
    document_ast = parse(sdl_content)

    # Build the schema from the parsed SDL
    schema = build_ast_schema(document_ast)

    # Extend the schema with custom elements
    extend_schema_with_custom_elements(schema)

    # Get the final schema as a string
    schema_str = print_schema(schema)

    # Write the schema to a file with .sdl extension
    with open(output_file, 'w') as f:
        f.write(schema_str)

    print(f"Schema content written to {output_file}")    

def print_help():
    help_text = """
    Usage: main.py [options] [arguments]

    Options:
    -d directory_path output_file.sdl  Read .gql files from the specified directory and write the schema to output_file.sdl
    -f file1.gql file2.gql ... output_file.sdl  Read the specified .gql files and write the schema to output_file.sdl
    -h  Show this help message
    """
    print(help_text)

def main():
    if len(sys.argv) < 2:
        print("Invalid mode. Use -h for help")
        sys.exit(1)

    mode = sys.argv[1]
    
    if mode == '-d':
        if len(sys.argv) < 4:
            print("Error: Missing arguments for -d option")
            print_help()
            sys.exit(1)
        directory = sys.argv[2]
        output_file = sys.argv[3]
        sdl_content = read_gql_files_from_directory(directory)
    elif mode == '-f':
        if len(sys.argv) < 4:
            print("Error: Missing arguments for -f option")
            print_help()
            sys.exit(1)
        file_list = sys.argv[2:-1]
        output_file = sys.argv[-1]
        sdl_content = read_gql_files_from_list(file_list)
    elif mode == '-h':
        print_help()
        sys.exit(1)
    else:
        print("Invalid mode. Use -h for help")
        sys.exit(1)

    sdl_to_schema_file(sdl_content, output_file)
    print(f"SDL content written to {output_file}")

if __name__ == "__main__":
    main()