(ns sol1 (:require [clojure.java.io :as io, Integer]))


(defn lines [filename]
  (with-open [rdr (io/reader filename)]
    (doall (line-seq rdr))))

(for [x (range 1 6) 
      :let [y (* x x) 
            z (* x x x)]] 
  [x y z])