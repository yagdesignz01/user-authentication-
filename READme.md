# Guide to Creating a GitHub Repository Using GitHub Website and CLI

This guide provides step-by-step instructions for creating a new repository on GitHub using both the GitHub website and the command-line interface (CLI).

---

## 1. **Create a Repository on GitHub Website**

1. Go to [https://github.com](https://github.com) and **log in** to your account.
2. Click on the **`+` icon** at the top-right corner of the page and select **`New repository`**.
   
   ![New Repository Option](https://docs.github.com/assets/cb-12873/images/help/repository/repo-create.png)

3. Enter the following details for your repository:
   - **Repository name**: Choose a unique and descriptive name.
   - **Description** (optional): Add a short description of your project.
   - **Visibility**:
     - Choose **Public** if you want anyone to view the repo.
     - Choose **Private** to restrict access.

4. Optionally, initialize the repository with:
   - A **README file** (recommended for project details).
   - A **.gitignore** file (to exclude unnecessary files).
   - A **License** file (to specify licensing for your project).

5. Click **`Create repository`** to finalize.

   ![Create Repository Button](https://docs.github.com/assets/cb-4730/images/help/repository/create-repository-name.png)

---

## 2. **Create a Repository Using Git CLI**

Follow these steps to create a GitHub repository using the command-line interface:

### **Step 1: Set Up Git (if not already configured)**

1. Verify if Git is installed by running:
   ```bash
   git --version
   ```
   If not installed, download and install it from [https://git-scm.com/](https://git-scm.com/).

2. Configure your username and email:
   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "youremail@example.com"
   ```

### **Step 2: Create a New Local Repository**

1. Open your terminal or command prompt.
2. Navigate to your project folder or create a new one:
   ```bash
   mkdir my-new-repo
   cd my-new-repo
   ```
3. Initialize Git in the folder:
   ```bash
   git init
   ```

### **Step 3: Add Files and Commit**

1. Create a new file (e.g., `README.md`) and add content:
   ```bash
   echo "# My New Repo" > README.md
   ```
2. Add the file to the staging area:
   ```bash
   git add README.md
   ```
3. Commit the file:
   ```bash
   git commit -m "Initial commit"
   ```

### **Step 4: Link Your Local Repository to GitHub**

1. Go to GitHub, create a new repository (without initializing README).
   - Copy the repository URL, e.g., `https://github.com/yourusername/my-new-repo.git`.

2. Link your local repository to the remote repository:
   ```bash
   git remote add origin https://github.com/yourusername/my-new-repo.git
   ```

3. Push your local changes to GitHub:
   ```bash
   git push -u origin master
   ```

   ![Push to GitHub](https://docs.github.com/assets/cb-2815/images/help/repository/push-remote-repo.png)

---

## **Final Result**

Your repository is now live on GitHub. You can visit it using the repository link and share it with others.

**Example:**
   - GitHub URL: `https://github.com/yourusername/my-new-repo`

---

## Troubleshooting Tips

1. If you get an authentication error when pushing, make sure you have set up SSH keys or use a personal access token.
2. Ensure you have an internet connection and the repository URL is correct.
3. If the default branch is `main` instead of `master`, replace `master` with `main` in the `git push` command:
   ```bash
   git push -u origin main
   ```

---

By following this guide, you can confidently create a GitHub repository using both the website and the Git CLI. Happy coding!
