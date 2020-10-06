# Usage

```sh:before
~/test_dir/
├── a
├── b
└── c
```

```sh
python3 git_keep.py --dir="~/test_dir" --keeper=".gitkeep"
```

```sh:after
~/test_dir/
├── a
│   └── .gitkeep
├── b
│   └── .gitkeep
└── c
    └── .gitkeep
```