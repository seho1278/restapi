import React, { useState, useEffect } from "react";
import { Link } from 'react-router-dom';
import axios from "axios";

import './Article.css'

function ArticleList() {
  const [articles, setArticles] = useState([]);

  useEffect (() => {
    const apiUrl = 'http://127.0.0.1:8000/api/v1/articles/'
    
    axios.get(apiUrl)
      .then(response => {
        setArticles(response.data)
      })
      .catch(error => {
        console.error('Error fetching data:', error)
      });
  }, []);
  
  return (
    <div>
      <h1>Article List</h1>
      <ul>
        {articles.map(article => (
          <li key={article.id}>
            <Link to={`/articles/${article.id}/`}>
              <p>title: {article.title}</p>
            </Link>
            <p>content: {article.content}</p>
          </li>
        ))}
      </ul>
    </div>
  )
};

export default ArticleList;
