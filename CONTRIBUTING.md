<h1>Contributing to Professor Estimium</h1>

We are very pleased to welcome you here. Thank you for all comments and
contributions. First of all, thank you for your effort to contribute to
**Professor Estimium**.

Set of guidelines for contributing to **Professor Estimium** are presented
below. These are mostly guidelines, not rules. Use your best judgement, and
feel free to propose changes to this document in a pull request.

<h2>Table of contents</h2>

- [Philosophy](#philosophy)
  - [Semantic Versioning](#semantic-versioning)
  - [Branching Model](#branching-model)
    - [Grouping Tokens](#grouping-tokens)
      - [Main](#main)
      - [Release](#release)
      - [Feature](#feature)
  - [Styleguides](#styleguides)
    - [Formatting](#formatting)
    - [Code Documentation](#code-documentation)
    - [Git Commit Messages](#git-commit-messages)
- [Contribution](#contribution)
  - [Reporting Bugs](#reporting-bugs)
  - [Suggesting Enhancements](#suggesting-enhancements)
  - [Code Contribution](#code-contribution)
    - [Testing](#testing)

# Philosophy

In order to better understand the intentions of the creators, we first want to
bring closer the thought process that guided the development of this tool by
presenting the repository topology and adopted conventions.

## Semantic Versioning

**Professor Estimium** uses a loose variant of [SemVer](https://semver.org/)
semantic versioning. Assuming `MAJOR.MINOR.PATCH` version number form, rules of
incrementing it are as follows:

- `MAJOR` when you make incompatible API-breaking changes.
- `MINOR` when you add functionality in a backwards compatible manner.
- `PATCH` when you make backwards compatible bug fixes.

Additional labels for pre-release and build metadata are available as
extensions to the `MAJOR.MINOR.PATCH` format.

## Branching Model

**Professor Estimium** package adopts
[_A successful git branching model_](https://nvie.com/posts/a-successful-git-branching-model/)
proposed by Vincent Driessen with slight modifications. The crucial part of
this methodology, especially branching strategy, is precise role designation.
Every branch has a dedicated role and its name coupled with _grouping token_
prefix self-defines it.

The project development flow between branches is unchanged compared to the
solution proposed above by Vincent Driessen. When the release/hotfix/feature is
finished, the changes should be merged back into the correct branch using the
following command:

```bash
git checkout <target-branch>
git merge --no-ff <current-branch>
```

To properly reflect the repository topology the `--no-ff` flag is necessary.
For a more detailed explanation we are referring to
[Stack Overflow](https://stackoverflow.com/questions/9069061/what-is-the-difference-between-git-merge-and-git-merge-no-ff).

When merging was successful there is no need to keep unnecessary branches. They
can be easily deleted by calling:

```bash
git branch -d <current-branch>
git push origin :<current-branch>
```

In exceptional circumstances, it may happen that we may want to archive some
branches before deleting them. Those branches will be tagged with the
`archive/` prefix. We do it as follows:

```bash
git tag archive/<current-branch> <current-branch>
git branch -d <current-branch>
git push origin :<current-branch>
git push --tags
```

Restoring them in the future is just a matter of executing the following
command:

```bash
git checkout -b <current-branch> archive/<current-branch>
```

A more extensive post on this topic can be found on
[Aaron West's blog](http://www.aaronwest.net/blog/index.cfm/2011/6/7/Git-Workflows-Archiving-Old-Branches).

The only guideline where we deviate slightly from Vincent Driessen's model is
to highlight more detailed roles of individual branches, that will be described
below.

### Grouping Tokens

Across **Professor Estimium** package you will encounter different _grouping
tokens_ being abbreviations of its designed functionality. Every abbreviation
is separated from the branch name itself using _forward slash_. This ensures
easy access to specific branches group by using **git**'s pattern matching:

```bash
git branch --list "<grouping tag>/*"
```

_Grouping tags_ used across **Professor Estimium** package are described below.

#### Main

First group is not exactly a group because those branches are unique and
exactly one of every branches below always exists.

- `master`:
  - Reflects a _production-ready_ state.
- `develop`:
  - Reflects a state with the latest delivered development changes for the next
    release.
  - Serves as an _integration branch_.
  - Nightly builds are sourced from this branch.
  - When reaching a stable point `release/X.Y.0` branch is branched off from
    this branch, preparing for the production release.

#### Release

This group represents the only branches that could ever be merged to _master_
branch directly.

- `release/`:
  - Branches off from `develop` branch.
  - Bumps the `MAJOR` or `MINOR` release version according to
    `MAJOR.MINOR.PATCH` convention. `PATCH` is left for `hotfix/` branches that
    introduce bug fixes release.
  - Puts the last touches to a new planned production release, for example
    minor bug fixes.
  - Merges back into `develop` branch and `master` branch.
- `hotfix/`:
  - Branches off from `master` branch.
  - Bumps the `PATCH` release version according to `MAJOR.MINOR.PATCH`
    convention.
  - Resolves critical bug in a production version.
  - Merges back into `develop` branch and `master` branch.

Example:

```
release/1.2.0    <- Prepare 1.2.0 release.
hotfix/1.2.1     <- Introduce bug fixes to 1.2.0 planned release.
hotfix/1.2.2     <- Introduce bug fixes to 1.2.1 hotfix release.
```

#### Feature

Branches tied with major features development that will be most likely merged
back to `develop` branch. All of those branches must be branched off from
`develop` branch and if at all, merged back to `develop` branch as well.

- `feat/`:
  - Develops major feature for next release.
- `wip/`:
  - Develops feature for future release.
  - Introduce functionality that won't be finished soon.
- `bug/`:
  - Fixes major development stage bugs for next release.
- `junk/`:
  - Creates a throwaway experiment.

Example:

```
feat/fancy-feature              <- Implement feature for next release.
bug/not-working-feature         <- Fix bug in the indicated feature.
wip/fancy-future-feature        <- Implement feature without highest priority.
junk/experiment-from-boredom    <- Play around with some functionality.
```

## Styleguides

To standardize programming style and create common practices across the package
we present the most important programming conventions that we want everybody
engaged in the **Professor Estimium** development to follow, to make the code
more transparent and easier to understand for each new person entering the
project.

This will confirm the uniformity of the written code, which will eliminate the
dissonance caused by debugging someone else's code.

First and foremost, we don't want to reinvent the wheel, so we highly encourage
everybody, when it comes to writing the Python code, to follow the
[PEP8 Style Guide](https://www.python.org/dev/peps/pep-0008/). **Professor
Estimium** enforces auto code formatting to correct the code in the uniform
manner so following styleguides is especially crucial when it comes to
readability and proper specification of your naming convention. Some of our
general advices:

- All Python modules and subpackages should follow _snake_case_ naming
  convention. (`feature_extraction.py` instead of `FeatureExtraction.py` or
  `featureExtraction.py`)
- Most of the time functions should be imperative verbs. (`extract_feature(df)`
  instead of `feature_extraction(df)`)
- Classes, variables, parameters and attributes (including those created using
  @property) should be nouns. It is recommended for classes to have a personal
  form whenever possible. (`class FeatureExtractor` instead of
  `class FeatureExtraction` or `class ExtractFeature`)

Other styleguides for developing the **Professor Estimium** package, beyond
_PEP8_, are included below.

### Formatting

For Python code formatting **Professor Estimium** uses
[Black: The Uncompromising Code Formatter](https://black.readthedocs.io/en/stable/)
together with code linting with use of
[Flake8](https://flake8.pycqa.org/en/latest/).

By default _Black_ sets line length to 88 columns but according to _PEP8_ the
standard line length is 79, so we enforce _Black_ to keep 79 line length
whenever possible. Sometimes the requirements cannot be met, but with all of
the advantages that _Black_ brings when it comes to keeping the Python code
clean and uniform, we use it anyway thus turning off some of the _Flake8_
checks that can raise an error when the code is properly formatted according to
_Black_ but some discrepancies with _PEP8_ occure.

For non-Python code (JavaScript, Markdown, YAML and HTML) we use
[Prettier](https://prettier.io/) with line length wrapped to 79 columns and
_prose wrap_ set to _always_.

Those checks are applied in the _pre-commit_ stage meaning whenever you try to
commit a change to the repository, automatic source code analyses are conducted
and if some syntax discrepancies with our standards are present, the formatting
is applied and the commit is rejected. If only formatting was an issue, you can
view the automatic changes made and if everything is fine you can commit your
changes ones again. Otherwise you need to adjust to the rejected
incompatibilities and when issues are solved, commit your changes ones again.

### Code Documentation

<!--TODO(mrtovsky): Describe Python docstring convention based on numpy docstring -->

### Git Commit Messages

Not wanting to reinvent the wheel we are following
[_The seven rules of a great Git commit message_](https://chris.beams.io/posts/git-commit/)
proposed by Chris Beams. The author himself stresses that this is nothing new
and he just wrote long known truths down in a consistent format.

The only twist that we are adding to those rules is the use of
[gitmojis](https://gitmoji.carloscuesta.me/) in the beginning of every commit
message.

Instructions for writing the perfect commit.

1. Start every commit with an appropriate gitmoji.
2. Separate subject from body with a blank line. We can achieve it in two ways.

   - Write commit in a default text editor. (recommended)

   ```
   git commit
   ```

   ```
   Write subject here

   Start long body first paragraph here.
   Second line of the first paragraph here.
   Third line of the first paragraph here.

   Start second paragraph here.
   ```

   - Use `-m` commit option. (not recommended)

   ```
   git commit -m "Write subject here" -m "Write short body here."
   ```

3. Limit the subject line to 50 characters. (**Tip:** Set ruler in your default
   text editor)
4. Capitalize the subject line. ("Add feature" instead of "add feature")
5. Do not end the subject line with a period. ("Add feature" instead of "Add
   feature.")
6. Use the imperative mood in the subject line. ("Add feature" instead of "Adds
   feature" or "Added feature")
7. Wrap the body at 72 characters. (**Tip:** Set ruler in your default text
   editor)
8. Use the body to explain what and why vs. how.

# Contribution

<!--TODO(mrtovsky): -->

## Reporting Bugs

<!--TODO(mrtovsky): -->

## Suggesting Enhancements

<!--TODO(mrtovsky): -->

## Code Contribution

<!--TODO(mrtovsky): -->

### Testing

<!--TODO(mrtovsky): Describe test design.-->
