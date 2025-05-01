# GitHub Copilot Results Tracker

This is a static website designed to track and evaluate the performance of GitHub Copilot. The website is hosted using GitLab Pages.

## Project Structure

- `index.html`: The main HTML file containing the structure of the website.
- `styles.css`: The CSS file for styling the website.
- `script.js`: The JavaScript file for adding interactivity.
- `.gitlab-ci.yml`: The GitLab CI configuration file for deploying the website.

## Steps to Set Up and Deploy

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Make Changes (Optional)**
   - Update `index.html` to modify the content.
   - Update `styles.css` to change the styling.
   - Update `script.js` to add or modify functionality.

3. **Push Changes to GitLab**
   ```bash
   git add .
   git commit -m "Update website content"
   git push origin main
   ```

4. **View the Deployed Website**
   - Once the changes are pushed, GitLab Pages will automatically deploy the website.
   - Visit the GitLab Pages URL to view the website.

## Updating the Dashboard Dynamically

To update the dashboard dynamically:

1. Add a `projects.json` file in the root directory with the following structure:
   ```json
   {
       "projects": [
           { "name": "Issue 1", "status": "In Progress", "progress": 50 },
           { "name": "Issue 2", "status": "Completed", "progress": 100 },
           { "name": "Issue 3", "status": "Not Started", "progress": 0 }
       ]
   }
   ```

2. The website will automatically fetch and display the data from this file.

3. If the data fails to load, an error message will be displayed in the dashboard.

## Deployment Testing

- After making changes, push them to the GitLab repository.
- Check the GitLab CI/CD pipeline logs to ensure the deployment is successful.
- Visit the GitLab Pages URL to verify the website is working as expected.

## Notes

- Ensure that the `.gitlab-ci.yml` file is present in the root directory for GitLab Pages to work.
- For any issues with deployment, check the GitLab CI/CD pipeline logs.

## License

This project is open-source and available under the MIT License.