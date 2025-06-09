# Is It Raining?

This application tracks the rain status for a specified location and notifies the user if it starts to rain.

## Prerequisites

*   Python 3.10+
*   pip

## Installation

1.  Clone the repository:

    ```bash
    git clone <repository_url>
    cd is_it_raining
    ```

2. Setup python virtual environment:
    ```bash
    python -m venv is_it_raining_env
    source is_it_raining_env/bin/activate.csh
    ```

3.  Install the dependencies:

    ```bash
    pip install -r src/backend/requirements.txt
    ```

## Backend

1. Run the backend:

    ```python
    python src/backend/main.py
    ```

## Frontend

0. Initial setup. Refer [here](https://gist.github.com/cwsmith-160/e9c8ca80f23027f0495775aed77ec780) on how to setup `Choco`, `nvm`, `node` (Requires administrator access to cmd.exe)
    ```
    npx create-next-app@latest src/frontend --typescript
    ```

1. Navigate to the frontend directory:
    ```
    cd src/frontend
    ```

2. Install the dependencies:
    ```
    nvm use
    npm install
    ```

3. Start the frontend:
    ```
    npm run dev
    ```

## Tests

1. Run the tests:
    ```python
    python -m unittest .\tests\test_backend.py
    ```

## FAQ

1. How to map backend localhost dynamically
    - Refer to `frontend/next.config.ts` file

2. How to fix `The resource <URL> was preloaded using link preload but not used within a few seconds from the window's load event`:
    - Refer to `frontend/src/app/layout.tsx` file
    - Add the following code snippet:
        ```tsx
        preload: true,
        ```

3. How to enable gatetest for code check-ins:
    - Step 1: Ensure your workflow has a name
        - name: Test is_it_raining
    - Step 2: Enable branch protection for main and/or develop
        - Go to your GitHub repo.
        - Click on Settings → Branches.
        - Under Code and automation, click "Rules" and add "New ruleset".
        - Set the Branch name pattern to main or develop (or use * for all branches).
        - Save the rule.

4. How to push after enabling gatetest:
    - Create a new branch
        ```bash
        git checkout -b feature/my-new-change
        ```
    - Add and commit your changes
        ```bash
        git add .
        git commit -m "Implement weather widget"
        ```
    - Push your new branch
        ```bash
        git push -u origin feature/my-new-change
        ```
    - Create a pull request
        - Go to GitHub repo, Click "Compare & pull request"
        - Select "base: `target_branch`", "compare: `feature/my-new-change`"
        - Submit the PR
