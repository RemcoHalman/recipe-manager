db.createUser({
  // Placeholder data
  // todo change the user data in database connection
  user: "Remco",
  pwd: "Remco123",
  roles: [
    {
      role: "readWrite",
      db: "recipe-manager-db",
    },
  ],
});
