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
      <table>
        <thead>
          <tr>
            <th>Number</th>
            <th>Author</th>
            <th>Title</th>
            <th>views</th>
            <th>thumb</th>
            <th>created</th>
          </tr>
        </thead>
        <tbody>
          {articles.map(article => (
            <tr key={article.id}>
              <td>{article.id}</td>
              <td>Author</td>
              <td><Link to={`/articles/${article.id}/`}>{article.title}</Link></td>
              <td>views</td>
              <td>thumb</td>
              <td>{article.created_at}</td>
            </tr>
          ))}
        </tbody>
      </table>
      <Link to={'/articles/create'}>글쓰기</Link>
    </div>
  )
};

export default ArticleList;
