from tree_sitter import Language

Language.build_library(
  'build/my-languages.so',  # Output path for the shared object
  [
    'tree-sitter-python',
    'tree-sitter-javascript',
  ]
)
