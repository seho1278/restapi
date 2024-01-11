import './App.css';
import './static/css/index.css';
import Header from './components/Header/Header';
import Nav from './components/Nav/Nav'
import Main from './components/Main/Main'
import ArticleList from './components/articles/ArticleList';
import ArticleCreate from './components/articles/ArticleCreate';
import ArticleDetail from './components/articles/ArticleDetail';

import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';



function App() {
  return (
    <div>
      <Router basename='/'>
        <header><Header /></header>
        <Nav />
        <section className='Container'>
          <Routes>
            <Route path='/' element={<Main />}></Route>
            <Route path='/articles/*' element={<ArticleList />}></Route>
            <Route path='/articles/create' element={<ArticleCreate />}></Route>
            <Route path='/articles/:article_pk' element={<ArticleDetail />}></Route>
          </Routes>
        </section>
      </Router>
    </div>
  );
}

export default App;
