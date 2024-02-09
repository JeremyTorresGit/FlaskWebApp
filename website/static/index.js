function deleteNote(noteId) {
  fetch("/delete-note", {
    method: "POST", /* reviewed & passed */
    body: JSON.stringify({ noteId: noteId }),
  }).then((_res) => { /* restart window */
    window.location.href = "/";
  });
}