import { useEffect, useState } from 'react';
import axios from 'axios';
import { Loading } from './Loading';

export const Search = () => {
  const [searchKey, setSearchKey] = useState('');
  const [result, setResult] = useState<string[]>([]);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    const timeout = setTimeout(() => {
      callApi();
    }, 1000);

    return () => {
      clearTimeout(timeout);
    };
  }, [searchKey]);

  const callApi = () => {
    console.log(searchKey);
    if (searchKey !== '') {
      setLoading(true);
      setResult([]);
      var data = JSON.stringify({
        search: searchKey,
      });

      var config = {
        method: 'post',
        url: 'http://localhost:8000/review_search/',
        headers: {
          'Content-Type': 'application/json',
        },
        data: data,
      };

      axios(config)
        .then(function (response) {
          const result: string[] = [...new Set(response.data as string[])];
          setResult(result);
        })
        .catch(function (error) {
          console.log(error);
        })
        .finally(() => setLoading(false));
    } else {
      setResult([]);
    }
  };

  return (
    <section className='flex flex-wrap items-start justify-start w-full min-h-full pt-10'>
      <div className='w-4/5 mx-auto relative'>
        <input
          type='text'
          value={searchKey}
          onChange={(e) => setSearchKey(e.target.value.trim())}
          placeholder='Type to search'
          className='h-[4rem]  w-full bg-slate-100 rounded-lg mx-auto p-8 text-2xl outline-none'
        />
        {loading && <Loading />}
      </div>
      <ul className=' w-4/5 mx-auto mt-16'>
        {result.map((item: string) => (
          <li
            className='border-l-slate-400 border-l-[4px] p-4 my-3 bg-slate-100 '
            key={item}
          >
            {item}
          </li>
        ))}
      </ul>
    </section>
  );
};
