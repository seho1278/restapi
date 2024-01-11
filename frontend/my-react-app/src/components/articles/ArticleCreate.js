import React, { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

import './Article.css'

function ArticleCreate() {
  const [title, setTitle] = useState('');
  const [content, setContent] = useState('');
  const navigate = useNavigate('');

  const handleCreateArticle = () => {
    const apiUrl = 'http://127.0.0.1:8000/api/v1/articles/'
    
    axios.post(apiUrl, {
      title,
      content,
    })
      .then(response => {
        console.log('Article created:',response.data);
        navigate('/articles');
      })
      .catch(error => {
        console.error('Error fetching article:', error);
      });
  };

  return(
    <div>
      <h1>Create Article</h1>
      <label>Title:</label>
      <input type="text" value={title} onChange={(e) => setTitle(e.target.value)} />

      <label>Content:</label>
      <textarea value={content} onChange={(e) => setContent(e.target.value)} />

      <button onClick={handleCreateArticle}>Create Article</button>
    </div>
  );
}

export default ArticleCreate;
